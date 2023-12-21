# CardLockingStrategy.ObtainLockCommandTimeoutSeconds - свойство
Таймаут на выполнение команд взятия блокировок в секундах. При таком таймауте
блокировка может быть взята в БД, но не взята с точки зрения сервера .NET.
Берём 15 минут, а не бесконечность, на случай, когда сервер СУБД безвозвратно
упал.
## __Definition
 **Пространство имён:** [Tessa.Cards](N_Tessa_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     protected virtual int ObtainLockCommandTimeoutSeconds { get; }
VB __Копировать
     Protected Overridable ReadOnly Property ObtainLockCommandTimeoutSeconds As Integer
    	Get
C++ __Копировать
     protected:
    virtual property int ObtainLockCommandTimeoutSeconds {
    	int get ();
    }
F# __Копировать
     abstract ObtainLockCommandTimeoutSeconds : int with get
    override ObtainLockCommandTimeoutSeconds : int with get
#### Значение свойства
[Int32](https://learn.microsoft.com/dotnet/api/system.int32)
##  __См. также
#### Ссылки
[CardLockingStrategy - ](T_Tessa_Cards_CardLockingStrategy.htm)
[Tessa.Cards - пространство имён](N_Tessa_Cards.htm)
