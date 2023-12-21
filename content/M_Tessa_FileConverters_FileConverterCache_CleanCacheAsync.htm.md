# FileConverterCache.CleanCacheAsync - метод
Очищает кэш от преобразованных файлов, доступ к содержимому которых выполнялся
раньше заданной даты, и возвращает результат операции по очистке кэша.
Возвращённое значение не равно null. В случае ошибок очистки исключение не
выбрасывается.
## __Definition
 **Пространство имён:** [Tessa.FileConverters](N_Tessa_FileConverters.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public Task<ValidationResult> CleanCacheAsync(
    	DateTime? oldestPreviewRequestTime = null,
    	CancellationToken cancellationToken = default
    )
VB __Копировать
     Public Function CleanCacheAsync ( 
    	Optional oldestPreviewRequestTime As DateTime? = Nothing,
    	Optional cancellationToken As CancellationToken = Nothing
    ) As Task(Of ValidationResult)
C++ __Копировать
     public:
    virtual Task<ValidationResult^>^ CleanCacheAsync(
    	Nullable<DateTime> oldestPreviewRequestTime = nullptr, 
    	CancellationToken cancellationToken = CancellationToken()
    ) sealed
F# __Копировать
     abstract CleanCacheAsync : 
            ?oldestPreviewRequestTime : Nullable<DateTime> * 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _oldestPreviewRequestTime = defaultArg oldestPreviewRequestTime null
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> Task<ValidationResult> 
    override CleanCacheAsync : 
            ?oldestPreviewRequestTime : Nullable<DateTime> * 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _oldestPreviewRequestTime = defaultArg oldestPreviewRequestTime null
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> Task<ValidationResult> 
#### Параметры
oldestPreviewRequestTime
[Nullable](https://learn.microsoft.com/dotnet/api/system.nullable-1)<[DateTime](https://learn.microsoft.com/dotnet/api/system.datetime)>
(Optional)
     Самая поздняя разрешённая дата, когда выполнялось обращение к файлу в кэше. Все файлы, к которым обращались раньше это даты, будут удалены из кэша. Значение null указывает, что из кэша будут удалены все файлы. 
cancellationToken
[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)
(Optional)
    Объект, посредством которого можно отменить асинхронную задачу.
#### Возвращаемое значение
[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)<[ValidationResult](T_Tessa_Platform_Validation_ValidationResult.htm)>  
Результат операции по очистке кэша. Возвращённое значение не равно null.
#### Реализации
[IFileConverterCache.CleanCacheAsync(Nullable<DateTime>,
CancellationToken)](M_Tessa_FileConverters_IFileConverterCache_CleanCacheAsync.htm)  
##  __См. также
#### Ссылки
[FileConverterCache - ](T_Tessa_FileConverters_FileConverterCache.htm)
[Tessa.FileConverters - пространство имён](N_Tessa_FileConverters.htm)
