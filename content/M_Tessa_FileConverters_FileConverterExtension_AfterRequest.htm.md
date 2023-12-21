# FileConverterExtension.AfterRequest - метод
Метод, выполняемый после конвертирования файлов, причём как в случае успеха,
так и при возникновении ошибок. Проверить успешность операции можно по
свойству context.RequestIsSuccessful. Файл после конвертации доступен в этом
методе по заданному в контексте пути. Если метод вернёт ошибку в результате
валидации или выбросит исключение, то результаты конвертации не будут
сохранены.
## __Definition
 **Пространство имён:** [Tessa.FileConverters](N_Tessa_FileConverters.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public virtual Task AfterRequest(
    	IFileConverterContext context
    )
VB __Копировать
     Public Overridable Function AfterRequest ( 
    	context As IFileConverterContext
    ) As Task
C++ __Копировать
     public:
    virtual Task^ AfterRequest(
    	IFileConverterContext^ context
    )
F# __Копировать
     abstract AfterRequest : 
            context : IFileConverterContext -> Task 
    override AfterRequest : 
            context : IFileConverterContext -> Task 
#### Параметры
context
[IFileConverterContext](T_Tessa_FileConverters_IFileConverterContext.htm)
    Контекст операции конвертации.
#### Возвращаемое значение
[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task)  
Асинхронная задача.
#### Реализации
[IFileConverterExtension.AfterRequest(IFileConverterContext)](M_Tessa_FileConverters_IFileConverterExtension_AfterRequest.htm)  
##  __Заметки
По умолчанию метод не выполняет действий.
##  __См. также
#### Ссылки
[FileConverterExtension - ](T_Tessa_FileConverters_FileConverterExtension.htm)
[Tessa.FileConverters - пространство имён](N_Tessa_FileConverters.htm)
