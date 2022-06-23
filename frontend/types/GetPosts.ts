export type GetPosts = Post[]

export type Post = {
  title: string,
  description: string,
  id: number,
  user_id: number,
  time_created: string,
  time_updated: string
}
