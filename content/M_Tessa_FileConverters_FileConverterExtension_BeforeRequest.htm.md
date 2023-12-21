# FileConverterExtension.BeforeRequest - метод
Метод, выполняемый перед конвертированием файлов. Файл после конвертации
недоступен в этом методе. Если метод вернёт ошибку в результате валидации или
выбросит исключение, то конвертация не будет выполнена.
## __Definition
 **Пространство имён:** [Tessa.FileConverters](N_Tessa_FileConverters.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public virtual Task BeforeRequest(
    	IFileConverterContext context
    )
VB __Копировать
     Public Overridable Function BeforeRequest ( 
    	context As IFileConverterContext
    ) As Task
C++ __Копировать
     public:
    virtual Task^ BeforeRequest(
    	IFileConverterContext^ context
    )
F# __Копировать
     abstract BeforeRequest : 
            context : IFileConverterContext -> Task 
    override BeforeRequest : 
            context : IFileConverterContext -> Task 
#### Параметры
context
[IFileConverterContext](T_Tessa_FileConverters_IFileConverterContext.htm)
    Контекст операции конвертации.
#### Возвращаемое значение
[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task)  
Асинхронная задача.
#### Реализации
[IFileConverterExtension.BeforeRequest(IFileConverterContext)](M_Tessa_FileConverters_IFileConverterExtension_BeforeRequest.htm)  
##  __Заметки
По умолчанию метод не выполняет действий.
##  __См. также
#### Ссылки
[FileConverterExtension - ](T_Tessa_FileConverters_FileConverterExtension.htm)
[Tessa.FileConverters - пространство имён](N_Tessa_FileConverters.htm)
