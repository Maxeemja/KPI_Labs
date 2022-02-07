import {Link, useMatch, useResolvedPath} from "react-router-dom";
import classNames from "classnames";

export const LabLink = ({ children, to, className, ...props }) => {
  let match = useMatch({ path: useResolvedPath(to).pathname, end: true });

  const linkClass = classNames('hover:bg-gray-200 rounded py-2 px-4 font-semibold tracking-wide', className, {
    'bg-violet-200': match,
  })

  return (
    <div>
      <Link
        className={linkClass}
        to={to}
        {...props}
      >
        {children}
      </Link>
    </div>
  );
}