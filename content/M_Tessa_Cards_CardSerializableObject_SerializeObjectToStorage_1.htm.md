# CardSerializableObject.SerializeObjectToStorage(Dictionary<String, Object>,
String, ISerializableObject) - метод
Сериализует объект в заданное хранилище Dictionary<string, object>.
## __Definition
 **Пространство имён:** [Tessa.Cards](N_Tessa_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     protected static void SerializeObjectToStorage(
    	[NotNullAttribute] Dictionary<string, Object> storage,
    	[NotNullAttribute] string key,
    	[CanBeNullAttribute] ISerializableObject obj
    )
VB __Копировать
     Protected Shared Sub SerializeObjectToStorage ( 
    	<NotNullAttribute> storage As Dictionary(Of String, Object),
    	<NotNullAttribute> key As String,
    	<CanBeNullAttribute> obj As ISerializableObject
    )
C++ __Копировать
     protected:
    static void SerializeObjectToStorage(
    	[NotNullAttribute] Dictionary<String^, Object^>^ storage, 
    	[NotNullAttribute] String^ key, 
    	[CanBeNullAttribute] ISerializableObject^ obj
    )
F# __Копировать
     static member SerializeObjectToStorage : 
            [<NotNullAttribute>] storage : Dictionary<string, Object> * 
            [<NotNullAttribute>] key : string * 
            [<CanBeNullAttribute>] obj : ISerializableObject -> unit 
#### Параметры
storage
[Dictionary](https://learn.microsoft.com/dotnet/api/system.collections.generic.dictionary-2)<[String](https://learn.microsoft.com/dotnet/api/system.string),
[Object](https://learn.microsoft.com/dotnet/api/system.object)>
    Хранилище, которое должно содержать сериализованные данные.
key [String](https://learn.microsoft.com/dotnet/api/system.string)
     Ключ, по которому сериализованные данные должны быть расположены в хранилище storage. 
obj [ISerializableObject](T_Tessa_Platform_Storage_ISerializableObject.htm)
    Объект, сериализация которого выполняется.
##  __См. также
#### Ссылки
[CardSerializableObject - ](T_Tessa_Cards_CardSerializableObject.htm)
[SerializeObjectToStorage -
перегрузка](Overload_Tessa_Cards_CardSerializableObject_SerializeObjectToStorage.htm)
[Tessa.Cards - пространство имён](N_Tessa_Cards.htm)
