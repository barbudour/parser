# ApplicationsWebProxy.TryGetModifiedAsync - метод
Возвращает дату изменения приложения и признак того, что приложение является
64-битным.
## __Definition
 **Пространство имён:**
[Tessa.Applications.Services.TessaServer](N_Tessa_Applications_Services_TessaServer.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public Task<(DateTime? Modified, bool Client64Bit)> TryGetModifiedAsync(
    	string applicationAlias,
    	bool? client64Bit,
    	CancellationToken cancellationToken = default
    )
VB __Копировать
     Public Function TryGetModifiedAsync ( 
    	applicationAlias As String,
    	client64Bit As Boolean?,
    	Optional cancellationToken As CancellationToken = Nothing
    ) As Task(Of (Modified As DateTime?, Client64Bit As Boolean))
C++ __Копировать
     public:
    Task<ValueTuple<Nullable<DateTime>, bool>>^ TryGetModifiedAsync(
    	String^ applicationAlias, 
    	Nullable<bool> client64Bit, 
    	CancellationToken cancellationToken = CancellationToken()
    )
F# __Копировать
     member TryGetModifiedAsync : 
            applicationAlias : string * 
            client64Bit : Nullable<bool> * 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> Task<ValueTuple<Nullable<DateTime>, bool>> 
#### Параметры
applicationAlias
[String](https://learn.microsoft.com/dotnet/api/system.string)
    Алиас приложения.
client64Bit
[Nullable](https://learn.microsoft.com/dotnet/api/system.nullable-1)<[Boolean](https://learn.microsoft.com/dotnet/api/system.boolean)>
     Признак того, что приложение является 64-битным. Укажите null, чтобы не фильтровать приложения по разрядности, и скачивать те из них, разрядность которых соответствует разрядности ОС или настройкам в карточке сотрудника. 
cancellationToken
[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)
(Optional)
    Объект, посредством которого можно отменить асинхронную задачу.
#### Возвращаемое значение
[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)<[ValueTuple](https://learn.microsoft.com/dotnet/api/system.valuetuple-2)<[Nullable](https://learn.microsoft.com/dotnet/api/system.nullable-1)<[DateTime](https://learn.microsoft.com/dotnet/api/system.datetime)>,
[Boolean](https://learn.microsoft.com/dotnet/api/system.boolean)>>  
Дата и время изменения приложения или null, если данные не удалось получить.
## __См. также
#### Ссылки
[ApplicationsWebProxy -
](T_Tessa_Applications_Services_TessaServer_ApplicationsWebProxy.htm)
[Tessa.Applications.Services.TessaServer - пространство
имён](N_Tessa_Applications_Services_TessaServer.htm)
