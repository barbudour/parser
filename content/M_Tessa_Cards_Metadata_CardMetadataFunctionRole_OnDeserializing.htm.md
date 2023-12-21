# CardMetadataFunctionRole.OnDeserializing - метод
Выполняется перед десериализацией объекта и всех его дочерних объектов из
элемента XML.
##  __Definition
 **Пространство имён:** [Tessa.Cards.Metadata](N_Tessa_Cards_Metadata.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     protected override void OnDeserializing(
    	SerializationMode mode
    )
VB __Копировать
     Protected Overrides Sub OnDeserializing ( 
    	mode As SerializationMode
    )
C++ __Копировать
     protected:
    virtual void OnDeserializing(
    	SerializationMode mode
    ) override
F# __Копировать
     abstract OnDeserializing : 
            mode : SerializationMode -> unit 
    override OnDeserializing : 
            mode : SerializationMode -> unit 
#### Параметры
mode [SerializationMode](T_Tessa_Cards_SerializationMode.htm)
    Способ, которым объект был сериализован.
##  __См. также
#### Ссылки
[CardMetadataFunctionRole -
](T_Tessa_Cards_Metadata_CardMetadataFunctionRole.htm)
[Tessa.Cards.Metadata - пространство имён](N_Tessa_Cards_Metadata.htm)
