// 読み込み確認(F12で確認)
console.log("cafe app JS loaded");

// DOM操作開始宣言
document.addEventListener("DOMContentLoaded", () => {
  // 1. delete-form を持つ要素をすべて取得する
  const deleteForms = document.querySelectorAll(".delete-form");

  // forEach: 最初から順にやってね for文みたいなの()の中身は名前自由
  deleteForms.forEach((form) => {
    // 対象の要素.addEventListener(出来事があったら（これならsubmit送信されたら)
    // event: ブラウザが自動で作ってくれる詰まった引数
    form.addEventListener("submit", (event) => {
      // 一度送信をストップする
      event.preventDefault();

      // どのカフェを消そうとしてるか
      // cafe_list.htmlから data-cafe-name の中身を引っ張る
      const cafeName = form.getAttribute("data-cafe-name") || "このカフェ";

      // 確認ダイアログを表示
      // window.confirm(ブラウザの標準ポップアップ) 変数を埋め込むためにバッククォートを使う！
      const isConfirmed = window.confirm(
        `「${cafeName}」を本当に削除しますか？`,
      );

      // okならフォーム送信を再開する
      if (isConfirmed) {
        form.submit();
      }
    });
  });
});
