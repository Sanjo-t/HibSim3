import streamlit as st

st.set_page_config(page_title="誹謗中傷AIシミュレーター", layout="centered")

st.title("誹謗中傷AIシミュレーター")
st.write("テスト投稿を入力すると、AIが毒性スコアやDM返信をシミュレートします。")

sample_post = st.text_area("投稿を入力してください：", "例：あれだけ前評判悪いのに、行く人がいてビックリ！")

if st.button("分析する"):
    # シミュレーション結果のモック
    st.subheader("分析結果")
    st.write("毒性スコア: 72/100")
    st.write("感情タイプ: 皮肉、無関心")

    st.subheader("自動生成されたDM例")
    st.write("『◯◯さんが行くのは自由ですが、少し寛容さが足りないように思えました。』")
