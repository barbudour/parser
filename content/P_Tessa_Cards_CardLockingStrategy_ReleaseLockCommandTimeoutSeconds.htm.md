# CardLockingStrategy.ReleaseLockCommandTimeoutSeconds - свойство
Таймаут на снятие блокировок в секундах. Берём 5 минут, а не бесконечность, на
случай, когда сервер СУБД безвозвратно упал.
## __Definition
 **Пространство имён:** [Tessa.Cards](N_Tessa_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     protected virtual int ReleaseLockCommandTimeoutSeconds { get; }
VB __Копировать
     Protected Overridable ReadOnly Property ReleaseLockCommandTimeoutSeconds As Integer
    	Get
C++ __Копировать
     protected:
    virtual property int ReleaseLockCommandTimeoutSeconds {
    	int get ();
    }
F# __Копировать
     abstract ReleaseLockCommandTimeoutSeconds : int with get
    override ReleaseLockCommandTimeoutSeconds : int with get
#### Значение свойства
[Int32](https://learn.microsoft.com/dotnet/api/system.int32)
##  __См. также
#### Ссылки
[CardLockingStrategy - ](T_Tessa_Cards_CardLockingStrategy.htm)
[Tessa.Cards - пространство имён](N_Tessa_Cards.htm)
