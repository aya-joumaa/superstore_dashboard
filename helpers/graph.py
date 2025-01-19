def prepare_the_bubbles_size_and_texts(store_data, x_axis_val, y_axis_val):
    hover_text = []
    for index, row in store_data.iterrows():
        hover_text.append(
            (
                    f'Order Id: {row["Order ID"]}<br>' +
                    f'{x_axis_val}: {row[x_axis_val]}<br>' +
                    f'{y_axis_val}: {row[y_axis_val]}<br>'
            )
        )

    return hover_text
