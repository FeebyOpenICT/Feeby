export interface InviteOnRevision {
  uuid: string;
  time_created: string;
  time_opened: string;
  time_finished: string;
  user: User;
}

export interface User {
  fullname: string;
  canvas_email: string;
  id: number;
}
