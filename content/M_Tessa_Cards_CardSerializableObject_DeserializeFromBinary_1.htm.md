# CardSerializableObject.DeserializeFromBinary(BinaryReader) - метод
Выполняет десериализацию текущего объекта и всех его дочерних объектов из
байтового потока.
##  __Definition
 **Пространство имён:** [Tessa.Cards](N_Tessa_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public void DeserializeFromBinary(
    	BinaryReader reader
    )
VB __Копировать
     Public Sub DeserializeFromBinary ( 
    	reader As BinaryReader
    )
C++ __Копировать
     public:
    void DeserializeFromBinary(
    	BinaryReader^ reader
    )
F# __Копировать
     member DeserializeFromBinary : 
            reader : BinaryReader -> unit 
#### Параметры
reader
[BinaryReader](https://learn.microsoft.com/dotnet/api/system.io.binaryreader)
    Объект, осуществляющий чтение из байтового потока.
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
