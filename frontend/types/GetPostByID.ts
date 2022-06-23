export interface GetPostByID {
  title: string;
  description: string;
  id: number;
  user_id: number;
  time_created: string;
  time_updated: string;
  revisions: Revision[];
  user: User;
}

export interface Revision {
  description: string;
  id: number;
  post_id: number;
  time_created: string;
  feedback: Feedback[];
}

export interface Feedback {
  description: string;
  id: number;
  time_created: string;
  rating: Rating;
  aspect: Aspect;
  reviewer: User;
}

export interface Aspect {
  title: string;
  short_description: string;
  description: string;
  external_url: string;
  id: number;
  time_created: string;
  time_updated: string;
  ratings: Rating[];
}

export interface Rating {
  title: string;
  short_description: string;
  description: string;
  id: number;
  time_created: string;
  time_updated: string;
}

export interface User {
  fullname: string;
  canvas_email: string;
  id: number;
}
