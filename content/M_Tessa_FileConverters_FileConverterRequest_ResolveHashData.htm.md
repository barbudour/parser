# FileConverterRequest.ResolveHashData - метод
Заполняет хеш-таблицу со свойствами объекта, которые влияют на хеш операции по
конвертации, по которому, в том числе, выполняется сравнение операций и их
результатов в кэше. По умолчанию учитываются значения свойств VersionID,
EventName, OutputFormat и Parameters.
## __Definition
 **Пространство имён:** [Tessa.FileConverters](N_Tessa_FileConverters.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     protected virtual void ResolveHashData(
    	Dictionary<string, Object> data
    )
VB __Копировать
     Protected Overridable Sub ResolveHashData ( 
    	data As Dictionary(Of String, Object)
    )
C++ __Копировать
     protected:
    virtual void ResolveHashData(
    	Dictionary<String^, Object^>^ data
    )
F# __Копировать
     abstract ResolveHashData : 
            data : Dictionary<string, Object> -> unit 
    override ResolveHashData : 
            data : Dictionary<string, Object> -> unit 
#### Параметры
data
[Dictionary](https://learn.microsoft.com/dotnet/api/system.collections.generic.dictionary-2)<[String](https://learn.microsoft.com/dotnet/api/system.string),
[Object](https://learn.microsoft.com/dotnet/api/system.object)>
     Хранилище, которое содержит сериализуемые данные для вычисления хеша. Обычно ключом является имя свойства в запросе, а значение - значение этого свойства. 
## __См. также
#### Ссылки
[FileConverterRequest - ](T_Tessa_FileConverters_FileConverterRequest.htm)
[Tessa.FileConverters - пространство имён](N_Tessa_FileConverters.htm)
