# GlobalEventAwaiter - конструктор
Создаёт экземпляр класса с указанием глобального события, ожидание которого
будет выполняться.
## __Definition
 **Пространство имён:** [Chronos.Platform.IPC](N_Chronos_Platform_IPC.htm)  
 **Сборка:** Chronos.Platform (в Chronos.Platform.dll) Версия: 3.6.0.17
C# __Копировать
     public GlobalEventAwaiter(
    	IGlobalEvent globalEvent
    )
VB __Копировать
     Public Sub New ( 
    	globalEvent As IGlobalEvent
    )
C++ __Копировать
     public:
    GlobalEventAwaiter(
    	IGlobalEvent^ globalEvent
    )
F# __Копировать
     new : 
            globalEvent : IGlobalEvent -> GlobalEventAwaiter
#### Параметры
globalEvent [IGlobalEvent](T_Chronos_Platform_IPC_IGlobalEvent.htm)
     Событие с глобально уникальным именем, используемое для синхронизации между процессами. 
## __См. также
#### Ссылки
[GlobalEventAwaiter - ](T_Chronos_Platform_IPC_GlobalEventAwaiter.htm)
[Chronos.Platform.IPC - пространство имён](N_Chronos_Platform_IPC.htm)
