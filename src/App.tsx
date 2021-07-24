import axios from "axios";
import { useState, Fragment } from "react";
import { toast } from "react-toastify";
import "./styles.css";

export default function App() {
  const [links, setLinks] = useState([]);
  const [data, setData] = useState<string[]>([]);
  const [label, setLabel] = useState<string>();

  const handleOnChange = (elem: string) => {
    if (data.indexOf(elem) !== -1) {
      setData((data) => data.filter((_elem) => elem !== _elem));
    } else {
      setData((data) => [...data, elem]);
    }
    console.log({ elem, data });
  };
  const handleSubmit = async () => {
    try {
      await axios.post<void>("http://localhost:8000/input", {
        title: label,
        accounts: "string",
        accountsId: "string"
      });
      const data = (
        await axios.get<{ accountIds: string; accounts: string }>(
          `http://localhost:8000/accounts/${label}`
        )
      ).data;
      setLinks(JSON.parse(data.accounts).acc as any);
      setData([]);
    } catch (err) {
      console.error(err);
      toast.error("Errored", err.toString());
    }
  };
  // useEffect(() => {
  //   setLabel(`https://source.unsplash.com/random/200x200/?${data.join(",")}`);
  // }, [data]);

  return (
    <div className="App">
      <form
        onSubmit={(e) => {
          e.preventDefault();
          handleSubmit();
        }}
      >
        <input
          onChange={(e) => setLabel(e.target.value)}
          type="search"
          name="search"
          id="search"
          placeholder="Search"
        />
        <input value="Submit" type="submit"></input>
      </form>
      {links.map((elem, index) => {
        return (
          <Fragment key={index}>
            <div className="wrapper">
              <input
                onClick={(e) => handleOnChange(elem)}
                type="checkbox"
                // value={elem}
              />
              {elem}
            </div>
          </Fragment>
        );
      })}
      <button
        onClick={async () => {
          try {
            await axios.post<void>(`http://localhost:8000/update/${label}`, {
              data: data.toString()
            });
          } catch (err) {
            console.error(err);
          }
        }}
      >
        Handle Update
      </button>
      <button
        onClick={async () => {
          try {
            await axios.get<void>(`http://localhost:8000/send/${label}`, {});
          } catch (err) {
            console.error(err);
          }
        }}
      >
        send message
      </button>
    </div>
  );
}
