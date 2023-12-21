# CardMetadataColumn - свойства
##  __Свойства
[CardTypeIDList](P_Tessa_Cards_Metadata_CardMetadataColumn_CardTypeIDList.htm)|
Список идентификаторов типов карточек, в которых используется колонка.  
---|---  
[ColumnType](P_Tessa_Cards_Metadata_CardMetadataColumn_ColumnType.htm)|  Тип
колонки.  
[ComplexColumnIndex](P_Tessa_Cards_Metadata_CardMetadataColumn_ComplexColumnIndex.htm)|
Уникальный в пределах таблицы отсчитываемый от нуля индекс, если текущая
колонка комплексная, или индекс комплексной колонки, в которую включена
текущая физическая колонка, или -1, если текущая физическая колонка не
включена в комплексную колонку.  
[DefaultValidValue](P_Tessa_Cards_Metadata_CardMetadataColumn_DefaultValidValue.htm)|
Значение колонки по умолчанию, которое может быть размещено в карточке и
всегда является валидным при сохранении. Определяется типом данных или
значением, заданным в схеме. Для комплексной колонки всегда возвращается null.  
[DefaultValue](P_Tessa_Cards_Metadata_CardMetadataColumn_DefaultValue.htm)|
Значение колонки по умолчанию, которое может быть размещено в карточке.
Определяется типом данных или значением, заданным в схеме. Для комплексной
колонки всегда возвращается null.  
[ID](P_Tessa_Cards_CardSerializableEntry_ID.htm)| Идентификатор объекта.  
(Унаследован от
[CardSerializableEntry](T_Tessa_Cards_CardSerializableEntry.htm))  
[IsReference](P_Tessa_Cards_Metadata_CardMetadataColumn_IsReference.htm)|
Признак того, что колонка является ссылочной и входит во внешний ключ при его
наличии. Значение актуально только для физических колонок.  
[IsSealed](P_Tessa_Cards_CardSerializableObject_IsSealed.htm)| Признак того,
что объект был защищён от изменений.  
(Унаследован от
[CardSerializableObject](T_Tessa_Cards_CardSerializableObject.htm))  
[MetadataType](P_Tessa_Cards_Metadata_CardMetadataColumn_MetadataType.htm)|
Тип данных, которые могут быть размещены в карточке.  
[Name](P_Tessa_Cards_CardSerializableEntry_Name.htm)| Отображаемое имя
объекта.  
(Унаследован от
[CardSerializableEntry](T_Tessa_Cards_CardSerializableEntry.htm))  
[ParentRowSection](P_Tessa_Cards_Metadata_CardMetadataColumn_ParentRowSection.htm)|
Секция, на строку которой ссылается текущая колонка, или null, если колонка не
ссылается на строку секции. Значение указывается только для комплексной
колонки, а также для физической, которая непосредственно ссылается на строку
секции.  
[Reference](P_Tessa_Cards_CardSerializableObject_Reference.htm)|  Имя
глобального объекта, на который ссылается данный объект.  
(Унаследован от
[CardSerializableObject](T_Tessa_Cards_CardSerializableObject.htm))  
[ReferencedSection](P_Tessa_Cards_Metadata_CardMetadataColumn_ReferencedSection.htm)|
Секция, на которую ссылается комплексная колонка, или null, если колонка
является физической.  
[XmlElementNameInternal](P_Tessa_Cards_Metadata_CardMetadataColumn_XmlElementNameInternal.htm)|
Имя XML-элемента, для которого выполняется сериализация и десериализация.  
(Переопределяет
[CardSerializableObject.XmlElementNameInternal](P_Tessa_Cards_CardSerializableObject_XmlElementNameInternal.htm))  
##  __См. также
#### Ссылки
[CardMetadataColumn - ](T_Tessa_Cards_Metadata_CardMetadataColumn.htm)
[Tessa.Cards.Metadata - пространство имён](N_Tessa_Cards_Metadata.htm)
