import { LabHeader } from "../../components/LabHeader";
import { Alg1 } from "./Alg1";
import { Alg2 } from "./Alg2";

export const Lab1 = () => {
	return (
		<div>
			<LabHeader num="1" topic="Поняття алгоритму. Задавання алгоритмів у вигляді блок-схем"/>

      <strong className="my-5 text-left text-lg">Лінійний алгоритм</strong>
      <hr  className="my-3"/>
      <Alg1/>
      <strong className="my-5 text-left text-lg">Розгалужений алгоритм</strong>
      <hr  className="my-3"/>
      <Alg2/>
		</div>
	);
};
