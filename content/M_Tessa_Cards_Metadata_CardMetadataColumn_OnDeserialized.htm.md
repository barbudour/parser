# CardMetadataColumn.OnDeserialized - метод
Выполняется после успешной десериализации объекта и всех его дочерних объектов
из элемента XML.
##  __Definition
 **Пространство имён:** [Tessa.Cards.Metadata](N_Tessa_Cards_Metadata.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     protected override void OnDeserialized(
    	SerializationMode mode
    )
VB __Копировать
     Protected Overrides Sub OnDeserialized ( 
    	mode As SerializationMode
    )
C++ __Копировать
     protected:
    virtual void OnDeserialized(
    	SerializationMode mode
    ) override
F# __Копировать
     abstract OnDeserialized : 
            mode : SerializationMode -> unit 
    override OnDeserialized : 
            mode : SerializationMode -> unit 
#### Параметры
mode [SerializationMode](T_Tessa_Cards_SerializationMode.htm)
    Способ, которым объект был сериализован.
##  __См. также
#### Ссылки
[CardMetadataColumn - ](T_Tessa_Cards_Metadata_CardMetadataColumn.htm)
[Tessa.Cards.Metadata - пространство имён](N_Tessa_Cards_Metadata.htm)
