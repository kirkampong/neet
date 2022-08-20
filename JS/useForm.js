import { useState } from "react";
import { useForm } from "react-hook-form";
import Header from "./Header";

export function App() {
  const { register, handleSubmit, errors } = useForm();
  const [data, setData] = useState("");

  return (
    <form onSubmit={handleSubmit((data) => setData(JSON.stringify(data)))}>
      <Header />
      <input {...register("firstName")} placeholder="First name" />
      <input 
        type="password" placeholder="Password" name="password" 
        ref={register({required:true, minLength:8})} //minLength{value:8, message:"too short"}
      />
      {errors.password && <p>Password is invalid</p>}
      <select {...register("category")}>
        <option value="">Select...</option>
        <option value="A">Option A</option>
        <option value="B">Option B</option>
      </select>
      <textarea {...register("aboutYou")} placeholder="About you" />
      <p>{data}</p>
      <input type="submit" />
    </form>
  );
}