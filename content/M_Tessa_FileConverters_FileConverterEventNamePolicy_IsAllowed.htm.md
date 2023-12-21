# FileConverterEventNamePolicy.IsAllowed - метод
Возвращает признак того, что выполнение методов расширения допустимо для
заданного имени события по конвертации файлов.
##  __Definition
 **Пространство имён:** [Tessa.FileConverters](N_Tessa_FileConverters.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public bool IsAllowed(
    	string eventName
    )
VB __Копировать
     Public Function IsAllowed ( 
    	eventName As String
    ) As Boolean
C++ __Копировать
     public:
    virtual bool IsAllowed(
    	String^ eventName
    ) sealed
F# __Копировать
     abstract IsAllowed : 
            eventName : string -> bool 
    override IsAllowed : 
            eventName : string -> bool 
#### Параметры
eventName [String](https://learn.microsoft.com/dotnet/api/system.string)
    Проверяемое имя события.
#### Возвращаемое значение
[Boolean](https://learn.microsoft.com/dotnet/api/system.boolean)  
true, если выполнение методов расширения допустимо для заданного имени события
по конвертации файлов; false в противном случае.
#### Реализации
[IFileConverterEventNamePolicy.IsAllowed(String)](M_Tessa_FileConverters_IFileConverterEventNamePolicy_IsAllowed.htm)  
##  __См. также
#### Ссылки
[FileConverterEventNamePolicy -
](T_Tessa_FileConverters_FileConverterEventNamePolicy.htm)
[Tessa.FileConverters - пространство имён](N_Tessa_FileConverters.htm)
