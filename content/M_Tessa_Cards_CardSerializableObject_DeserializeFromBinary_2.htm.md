# CardSerializableObject.DeserializeFromBinary(Stream) - метод
Выполняет десериализацию текущего объекта и всех его дочерних объектов из
байтового потока.
##  __Definition
 **Пространство имён:** [Tessa.Cards](N_Tessa_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public void DeserializeFromBinary(
    	Stream stream
    )
VB __Копировать
     Public Sub DeserializeFromBinary ( 
    	stream As Stream
    )
C++ __Копировать
     public:
    void DeserializeFromBinary(
    	Stream^ stream
    )
F# __Копировать
     member DeserializeFromBinary : 
            stream : Stream -> unit 
#### Параметры
stream [Stream](https://learn.microsoft.com/dotnet/api/system.io.stream)
    Байтовый поток, из которого осуществляется чтение.
##  __Исключения
[Tessa.Platform.ObjectSealedException]| Произведена попытка изменения объекта,
защищённого от изменений.  
---|---  
##  __См. также
#### Ссылки
[CardSerializableObject - ](T_Tessa_Cards_CardSerializableObject.htm)
[DeserializeFromBinary -
перегрузка](Overload_Tessa_Cards_CardSerializableObject_DeserializeFromBinary.htm)
[Tessa.Cards - пространство имён](N_Tessa_Cards.htm)
[Tessa.Platform.ObjectSealedException]
