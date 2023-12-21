# IFileConverterEventNamePolicy.IsAllowed - метод
Возвращает признак того, что выполнение методов расширения допустимо для
заданного имени события по конвертации файлов.
##  __Definition
 **Пространство имён:** [Tessa.FileConverters](N_Tessa_FileConverters.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     bool IsAllowed(
    	string eventName
    )
VB __Копировать
     Function IsAllowed ( 
    	eventName As String
    ) As Boolean
C++ __Копировать
     bool IsAllowed(
    	String^ eventName
    )
F# __Копировать
     abstract IsAllowed : 
            eventName : string -> bool 
#### Параметры
eventName [String](https://learn.microsoft.com/dotnet/api/system.string)
    Проверяемое имя события.
#### Возвращаемое значение
[Boolean](https://learn.microsoft.com/dotnet/api/system.boolean)  
true, если выполнение методов расширения допустимо для заданного имени события
по конвертации файлов; false в противном случае.
## __См. также
#### Ссылки
[IFileConverterEventNamePolicy -
](T_Tessa_FileConverters_IFileConverterEventNamePolicy.htm)
[Tessa.FileConverters - пространство имён](N_Tessa_FileConverters.htm)
