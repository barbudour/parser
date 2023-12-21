# CardExtensionContext.CancellationToken - свойство
Объект, посредством которого можно отменить асинхронную задачу.
##  __Definition
 **Пространство имён:** [Tessa.Cards.Extensions](N_Tessa_Cards_Extensions.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public CancellationToken CancellationToken { get; set; }
VB __Копировать
     Public Property CancellationToken As CancellationToken
    	Get
    	Set
C++ __Копировать
     public:
    virtual property CancellationToken CancellationToken {
    	CancellationToken get () sealed;
    	void set (CancellationToken value) sealed;
    }
F# __Копировать
     abstract CancellationToken : CancellationToken with get, set
    override CancellationToken : CancellationToken with get, set
#### Значение свойства
[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)
#### Реализации
[IExtensionContext.CancellationToken](P_Tessa_Extensions_IExtensionContext_CancellationToken.htm)  
##  __Заметки
Не изменяйте значение этого свойства в процессе выполнения расширений.
##  __См. также
#### Ссылки
[CardExtensionContext - ](T_Tessa_Cards_Extensions_CardExtensionContext.htm)
[Tessa.Cards.Extensions - пространство имён](N_Tessa_Cards_Extensions.htm)
