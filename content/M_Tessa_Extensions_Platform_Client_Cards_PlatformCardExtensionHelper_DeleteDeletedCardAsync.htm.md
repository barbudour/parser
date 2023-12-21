# PlatformCardExtensionHelper.DeleteDeletedCardAsync - метод
Выполняет удаление удалённой карточки из корзины.
## __Definition
 **Пространство имён:**
[Tessa.Extensions.Platform.Client.Cards](N_Tessa_Extensions_Platform_Client_Cards.htm)  
 **Сборка:** Tessa.UI (в Tessa.UI.dll) Версия: 3.6.0.17
C# __Копировать
     public static Task DeleteDeletedCardAsync(
    	IUIContext context,
    	CancellationToken cancellationToken = default
    )
VB __Копировать
     Public Shared Function DeleteDeletedCardAsync ( 
    	context As IUIContext,
    	Optional cancellationToken As CancellationToken = Nothing
    ) As Task
C++ __Копировать
     public:
    static Task^ DeleteDeletedCardAsync(
    	IUIContext^ context, 
    	CancellationToken cancellationToken = CancellationToken()
    )
F# __Копировать
     static member DeleteDeletedCardAsync : 
            context : IUIContext * 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> Task 
#### Параметры
context [IUIContext](T_Tessa_UI_IUIContext.htm)
    Контекст с редактором, в котором открыта удалённая карточка.
cancellationToken
[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)
(Optional)
    Объект, посредством которого можно отменить асинхронную задачу.
#### Возвращаемое значение
[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task)  
Асинхронная задача.
##  __См. также
#### Ссылки
[PlatformCardExtensionHelper -
](T_Tessa_Extensions_Platform_Client_Cards_PlatformCardExtensionHelper.htm)
[Tessa.Extensions.Platform.Client.Cards - пространство
имён](N_Tessa_Extensions_Platform_Client_Cards.htm)
