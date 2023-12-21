# CardSerializableObject.DeserializeFromBinary(Byte[]) - метод
Выполняет десериализацию текущего объекта и всех его дочерних объектов из
массива байт.
##  __Definition
 **Пространство имён:** [Tessa.Cards](N_Tessa_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public void DeserializeFromBinary(
    	byte[] data
    )
VB __Копировать
     Public Sub DeserializeFromBinary ( 
    	data As Byte()
    )
C++ __Копировать
     public:
    void DeserializeFromBinary(
    	array<unsigned char>^ data
    )
F# __Копировать
     member DeserializeFromBinary : 
            data : byte[] -> unit 
#### Параметры
data [Byte](https://learn.microsoft.com/dotnet/api/system.byte)[]
    Массива байт, содержащий сериализованные данные.
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
