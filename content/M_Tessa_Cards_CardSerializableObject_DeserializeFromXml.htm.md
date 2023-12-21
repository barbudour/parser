# CardSerializableObject.DeserializeFromXml(Stream) - метод
Выполняет десериализацию объекта из XML из заданного потока.
## __Definition
 **Пространство имён:** [Tessa.Cards](N_Tessa_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public void DeserializeFromXml(
    	Stream stream
    )
VB __Копировать
     Public Sub DeserializeFromXml ( 
    	stream As Stream
    )
C++ __Копировать
     public:
    void DeserializeFromXml(
    	Stream^ stream
    )
F# __Копировать
     member DeserializeFromXml : 
            stream : Stream -> unit 
#### Параметры
stream [Stream](https://learn.microsoft.com/dotnet/api/system.io.stream)
    Поток, из которого читаются данные объекта, сериализованные в XML.
##  __Исключения
[Tessa.Platform.ObjectSealedException]| Произведена попытка изменения объекта,
защищённого от изменений.  
---|---  
##  __См. также
#### Ссылки
[CardSerializableObject - ](T_Tessa_Cards_CardSerializableObject.htm)
[DeserializeFromXml -
перегрузка](Overload_Tessa_Cards_CardSerializableObject_DeserializeFromXml.htm)
[Tessa.Cards - пространство имён](N_Tessa_Cards.htm)
[Tessa.Platform.ObjectSealedException]
