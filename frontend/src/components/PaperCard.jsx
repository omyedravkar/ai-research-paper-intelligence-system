function PaperCard({ paper }) {

    return (

        <div className="paper-card">

            <h2>{paper.title}</h2>

            <p className="similarity">

                Similarity : {(paper.similarity * 100).toFixed(2)}%

            </p>

            <p className="category">
                Category : {paper.classification}
            </p>

            <p className="confidence">
                Confidence : {(paper.classification_score * 100).toFixed(1)}%
            </p>

            <h4>Summary</h4>

            <p>{paper.summary}</p>

            <h4>Keywords</h4>

            <div className="badges">

                {paper.keywords.map((keyword, index) => (

                    <span
                        key={index}
                        className="badge"
                    >

                        {keyword[0]}

                    </span>

                ))}

            </div>

            <h4>Named Entities</h4>

            <div className="badges">

                {paper.entities.map((entity, index) => (

                    <span
                        key={index}
                        className="badge entity"
                    >

                        {entity.text}

                    </span>

                ))}

            </div>

        </div>

    );

}

export default PaperCard;