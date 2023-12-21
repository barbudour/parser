# NumberContext.Session - свойство
Сессия текущего пользователя.
##  __Definition
 **Пространство имён:** [Tessa.Cards.Numbers](N_Tessa_Cards_Numbers.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public ISession Session { get; }
VB __Копировать
     Public ReadOnly Property Session As ISession
    	Get
C++ __Копировать
     public:
    virtual property ISession^ Session {
    	ISession^ get () sealed;
    }
F# __Копировать
     abstract Session : ISession with get
    override Session : ISession with get
#### Значение свойства
[ISession](T_Tessa_Platform_Runtime_ISession.htm)
#### Реализации
[INumberDependencies.Session](P_Tessa_Cards_Numbers_INumberDependencies_Session.htm)  
##  __Заметки
Значение свойства никогда не равно null.
## __См. также
#### Ссылки
[NumberContext - ](T_Tessa_Cards_Numbers_NumberContext.htm)
[Tessa.Cards.Numbers - пространство имён](N_Tessa_Cards_Numbers.htm)
