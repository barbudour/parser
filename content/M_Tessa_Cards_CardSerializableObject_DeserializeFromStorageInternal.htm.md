# CardSerializableObject.DeserializeFromStorageInternal - метод
Выполняет десериализацию объекта и всех его дочерних объектов из хранилища
Dictionary<string, object>.
## __Definition
 **Пространство имён:** [Tessa.Cards](N_Tessa_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     protected virtual void DeserializeFromStorageInternal(
    	Dictionary<string, Object> storage
    )
VB __Копировать
     Protected Overridable Sub DeserializeFromStorageInternal ( 
    	storage As Dictionary(Of String, Object)
    )
C++ __Копировать
     protected:
    virtual void DeserializeFromStorageInternal(
    	Dictionary<String^, Object^>^ storage
    )
F# __Копировать
     abstract DeserializeFromStorageInternal : 
            storage : Dictionary<string, Object> -> unit 
    override DeserializeFromStorageInternal : 
            storage : Dictionary<string, Object> -> unit 
#### Параметры
storage
[Dictionary](https://learn.microsoft.com/dotnet/api/system.collections.generic.dictionary-2)<[String](https://learn.microsoft.com/dotnet/api/system.string),
[Object](https://learn.microsoft.com/dotnet/api/system.object)>
    Хранилище, в котором содержатся сериализованные данные.
##  __См. также
#### Ссылки
[CardSerializableObject - ](T_Tessa_Cards_CardSerializableObject.htm)
[Tessa.Cards - пространство имён](N_Tessa_Cards.htm)
