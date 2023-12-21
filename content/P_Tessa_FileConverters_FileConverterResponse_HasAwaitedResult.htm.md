# FileConverterResponse.HasAwaitedResult - свойство
Признак того, что ожидание результата было выполнено и результат был получен
(успешный или с ошибками). Если значение равно false, то метод получения
содержимого файла
[Tessa.FileConverters.IFileConverterResponse.GetStreamOrThrow] выбросит
исключение.
## __Definition
 **Пространство имён:** [Tessa.FileConverters](N_Tessa_FileConverters.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public bool HasAwaitedResult { get; }
VB __Копировать
     Public ReadOnly Property HasAwaitedResult As Boolean
    	Get
C++ __Копировать
     public:
    virtual property bool HasAwaitedResult {
    	bool get () sealed;
    }
F# __Копировать
     abstract HasAwaitedResult : bool with get
    override HasAwaitedResult : bool with get
#### Значение свойства
[Boolean](https://learn.microsoft.com/dotnet/api/system.boolean)
#### Реализации
[IFileConverterResponse.HasAwaitedResult](P_Tessa_FileConverters_IFileConverterResponse_HasAwaitedResult.htm)  
##  __См. также
#### Ссылки
[FileConverterResponse - ](T_Tessa_FileConverters_FileConverterResponse.htm)
[Tessa.FileConverters - пространство имён](N_Tessa_FileConverters.htm)
