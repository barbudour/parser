# GetCatalogContainerDelegateAsync - делегат
Возвращает контейнер получения зависимостей для каталога приложений
## __Definition
 **Пространство имён:** [Tessa.Applications](N_Tessa_Applications.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
    [NotNullAttribute]
    public delegate ValueTask<IUnityContainer> GetCatalogContainerDelegateAsync(
    	[NotNullAttribute] IApplicationCatalog catalog,
    	CancellationToken cancellationToken = default
    )
VB __Копировать
    <NotNullAttribute>
    Public Delegate Function GetCatalogContainerDelegateAsync ( 
    	<NotNullAttribute> catalog As IApplicationCatalog,
    	Optional cancellationToken As CancellationToken = Nothing
    ) As ValueTask(Of IUnityContainer)
C++ __Копировать
    [NotNullAttribute]
    public delegate ValueTask<IUnityContainer^> GetCatalogContainerDelegateAsync(
    	[NotNullAttribute] IApplicationCatalog^ catalog, 
    	CancellationToken cancellationToken = CancellationToken()
    )
F# __Копировать
     [<NotNullAttribute>]
    type GetCatalogContainerDelegateAsync = 
        delegate of 
            [<NotNullAttribute>] catalog : IApplicationCatalog * 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> ValueTask<IUnityContainer>
#### Параметры
catalog [IApplicationCatalog](T_Tessa_Applications_IApplicationCatalog.htm)
    Каталог приложений
cancellationToken
[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)
(Optional)
    Объект, посредством которого можно отменить асинхронную задачу.
#### Возвращаемое значение
[ValueTask](https://learn.microsoft.com/dotnet/api/system.threading.tasks.valuetask-1)<IUnityContainer>  
Контейнер получения зависимостей
##  __См. также
#### Ссылки
[Tessa.Applications - пространство имён](N_Tessa_Applications.htm)
