# CardSerializableObject.DeserializeObjectFromStorage(Dictionary<String,
Object>, String) - метод
Десериализует объект из заданного хранилища Dictionary<string, object>.
## __Definition
 **Пространство имён:** [Tessa.Cards](N_Tessa_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     protected static SerializableObject DeserializeObjectFromStorage(
    	[NotNullAttribute] Dictionary<string, Object> storage,
    	[NotNullAttribute] string key
    )
VB __Копировать
     Protected Shared Function DeserializeObjectFromStorage ( 
    	<NotNullAttribute> storage As Dictionary(Of String, Object),
    	<NotNullAttribute> key As String
    ) As SerializableObject
C++ __Копировать
     protected:
    static SerializableObject^ DeserializeObjectFromStorage(
    	[NotNullAttribute] Dictionary<String^, Object^>^ storage, 
    	[NotNullAttribute] String^ key
    )
F# __Копировать
     static member DeserializeObjectFromStorage : 
            [<NotNullAttribute>] storage : Dictionary<string, Object> * 
            [<NotNullAttribute>] key : string -> SerializableObject 
#### Параметры
storage
[Dictionary](https://learn.microsoft.com/dotnet/api/system.collections.generic.dictionary-2)<[String](https://learn.microsoft.com/dotnet/api/system.string),
[Object](https://learn.microsoft.com/dotnet/api/system.object)>
    Хранилище, содержащее сериализованные данные.
key [String](https://learn.microsoft.com/dotnet/api/system.string)
     Ключ, по которому сериализованные данные расположены в хранилище storage. 
#### Возвращаемое значение
[SerializableObject](T_Tessa_Platform_Storage_SerializableObject.htm)  
Десериализованный объект.
##  __См. также
#### Ссылки
[CardSerializableObject - ](T_Tessa_Cards_CardSerializableObject.htm)
[DeserializeObjectFromStorage -
перегрузка](Overload_Tessa_Cards_CardSerializableObject_DeserializeObjectFromStorage.htm)
[Tessa.Cards - пространство имён](N_Tessa_Cards.htm)
