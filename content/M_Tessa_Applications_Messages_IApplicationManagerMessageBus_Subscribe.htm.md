# IApplicationManagerMessageBus.Subscribe - метод
Вызывает подписку объекта observer на сообщения поступающие в шину данных
## __Definition
 **Пространство имён:**
[Tessa.Applications.Messages](N_Tessa_Applications_Messages.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
    [CanBeNullAttribute]
    IDisposable Subscribe(
    	[NotNullAttribute] IApplicationMessageObserver observer,
    	[NotNullAttribute] Func<ApplicationMessage, bool> messagePolicy
    )
VB __Копировать
    <CanBeNullAttribute>
    Function Subscribe ( 
    	<NotNullAttribute> observer As IApplicationMessageObserver,
    	<NotNullAttribute> messagePolicy As Func(Of ApplicationMessage, Boolean)
    ) As IDisposable
C++ __Копировать
    [CanBeNullAttribute]
    IDisposable^ Subscribe(
    	[NotNullAttribute] IApplicationMessageObserver^ observer, 
    	[NotNullAttribute] Func<ApplicationMessage^, bool>^ messagePolicy
    )
F# __Копировать
     [<CanBeNullAttribute>]
    abstract Subscribe : 
            [<NotNullAttribute>] observer : IApplicationMessageObserver * 
            [<NotNullAttribute>] messagePolicy : Func<ApplicationMessage, bool> -> IDisposable 
#### Параметры
observer
[IApplicationMessageObserver](T_Tessa_Applications_Services_ApplicationManager_IApplicationMessageObserver.htm)
     Объект подписывающийся на сообщения шины данных 
messagePolicy
[Func](https://learn.microsoft.com/dotnet/api/system.func-2)<[ApplicationMessage](T_Tessa_Applications_Messages_ApplicationMessage.htm),
[Boolean](https://learn.microsoft.com/dotnet/api/system.boolean)>
     Политика фильтрации сообщений 
#### Возвращаемое значение
[IDisposable](https://learn.microsoft.com/dotnet/api/system.idisposable)  
Объект при вызове метода
[Dispose()](https://learn.microsoft.com/dotnet/api/system.idisposable.dispose#system-
idisposable-dispose) будет произведена отписка от сообщений шины данных или
null в случае не удачной подписки.
## __См. также
#### Ссылки
[IApplicationManagerMessageBus -
](T_Tessa_Applications_Messages_IApplicationManagerMessageBus.htm)
[Tessa.Applications.Messages - пространство
имён](N_Tessa_Applications_Messages.htm)
