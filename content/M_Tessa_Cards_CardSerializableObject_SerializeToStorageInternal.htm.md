# CardSerializableObject.SerializeToStorageInternal - метод
Выполняет сериализацию текущего объекта и всех его дочерних объектов в
хранилище Dictionary<string, object>.
## __Definition
 **Пространство имён:** [Tessa.Cards](N_Tessa_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     protected virtual void SerializeToStorageInternal(
    	Dictionary<string, Object> storage
    )
VB __Копировать
     Protected Overridable Sub SerializeToStorageInternal ( 
    	storage As Dictionary(Of String, Object)
    )
C++ __Копировать
     protected:
    virtual void SerializeToStorageInternal(
    	Dictionary<String^, Object^>^ storage
    )
F# __Копировать
     abstract SerializeToStorageInternal : 
            storage : Dictionary<string, Object> -> unit 
    override SerializeToStorageInternal : 
            storage : Dictionary<string, Object> -> unit 
#### Параметры
storage
[Dictionary](https://learn.microsoft.com/dotnet/api/system.collections.generic.dictionary-2)<[String](https://learn.microsoft.com/dotnet/api/system.string),
[Object](https://learn.microsoft.com/dotnet/api/system.object)>
    Хранилище, в которое будут сериализованы данные.
##  __См. также
#### Ссылки
[CardSerializableObject - ](T_Tessa_Cards_CardSerializableObject.htm)
[Tessa.Cards - пространство имён](N_Tessa_Cards.htm)
