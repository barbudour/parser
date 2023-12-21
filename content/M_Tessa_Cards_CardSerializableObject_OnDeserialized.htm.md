# CardSerializableObject.OnDeserialized - метод
Выполняется после успешной десериализации объекта и всех его дочерних объектов
из элемента XML.
##  __Definition
 **Пространство имён:** [Tessa.Cards](N_Tessa_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     protected virtual void OnDeserialized(
    	SerializationMode mode
    )
VB __Копировать
     Protected Overridable Sub OnDeserialized ( 
    	mode As SerializationMode
    )
C++ __Копировать
     protected:
    virtual void OnDeserialized(
    	SerializationMode mode
    )
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
[CardSerializableObject - ](T_Tessa_Cards_CardSerializableObject.htm)
[Tessa.Cards - пространство имён](N_Tessa_Cards.htm)
