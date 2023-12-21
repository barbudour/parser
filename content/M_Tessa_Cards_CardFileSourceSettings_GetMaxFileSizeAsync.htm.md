# CardFileSourceSettings.GetMaxFileSizeAsync - метод
Максимальный размер файла в байтах, для которого разрешена загрузка в систему,
или null, если ограничения по размеру отсутствует. Свойство может
использоваться на клиенте и на сервере.
## __Definition
 **Пространство имён:** [Tessa.Cards](N_Tessa_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public ValueTask<long?> GetMaxFileSizeAsync(
    	CancellationToken cancellationToken = default
    )
VB __Копировать
     Public Function GetMaxFileSizeAsync ( 
    	Optional cancellationToken As CancellationToken = Nothing
    ) As ValueTask(Of Long?)
C++ __Копировать
     public:
    virtual ValueTask<Nullable<long long>> GetMaxFileSizeAsync(
    	CancellationToken cancellationToken = CancellationToken()
    ) sealed
F# __Копировать
     abstract GetMaxFileSizeAsync : 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> ValueTask<Nullable<int64>> 
    override GetMaxFileSizeAsync : 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> ValueTask<Nullable<int64>> 
#### Параметры
cancellationToken
[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)
(Optional)
    Объект, посредством которого можно отменить асинхронную задачу.
#### Возвращаемое значение
[ValueTask](https://learn.microsoft.com/dotnet/api/system.threading.tasks.valuetask-1)<[Nullable](https://learn.microsoft.com/dotnet/api/system.nullable-1)<[Int64](https://learn.microsoft.com/dotnet/api/system.int64)>>  
Асинхронная задача.
#### Реализации
[ICardFileSourceSettings.GetMaxFileSizeAsync(CancellationToken)](M_Tessa_Cards_ICardFileSourceSettings_GetMaxFileSizeAsync.htm)  
##  __См. также
#### Ссылки
[CardFileSourceSettings - ](T_Tessa_Cards_CardFileSourceSettings.htm)
[Tessa.Cards - пространство имён](N_Tessa_Cards.htm)
