# LinuxGlobalEvent.ResetCore - метод
Переводит событие в несигнальное состояние, при этом все ожидающие событие
подписчики получают управление.
## __Definition
 **Пространство имён:** [Chronos.Platform.IPC](N_Chronos_Platform_IPC.htm)  
 **Сборка:** Chronos.Platform.Linux (в Chronos.Platform.Linux.dll) Версия:
3.6.0.17
C# __Копировать
     protected override void ResetCore()
VB __Копировать
     Protected Overrides Sub ResetCore
C++ __Копировать
     protected:
    virtual void ResetCore() override
F# __Копировать
     abstract ResetCore : unit -> unit 
    override ResetCore : unit -> unit 
## __См. также
#### Ссылки
[LinuxGlobalEvent - ](T_Chronos_Platform_IPC_LinuxGlobalEvent.htm)
[Chronos.Platform.IPC - пространство имён](N_Chronos_Platform_IPC.htm)
