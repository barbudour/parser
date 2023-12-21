# LinuxChronosPlatformDependencies.CreateGlobalEvent - метод
Создаёт событие по глобально уникальному имени, который можно использовать для
синхронизации процессов как минимум в пределах сессии пользователя и всех
процессов в ней.
## __Definition
 **Пространство имён:** [Chronos.Platform](N_Chronos_Platform.htm)  
 **Сборка:** Chronos.Platform.Linux (в Chronos.Platform.Linux.dll) Версия:
3.6.0.17
C# __Копировать
     public override IGlobalEvent CreateGlobalEvent(
    	string name
    )
VB __Копировать
     Public Overrides Function CreateGlobalEvent ( 
    	name As String
    ) As IGlobalEvent
C++ __Копировать
     public:
    virtual IGlobalEvent^ CreateGlobalEvent(
    	String^ name
    ) override
F# __Копировать
     abstract CreateGlobalEvent : 
            name : string -> IGlobalEvent 
    override CreateGlobalEvent : 
            name : string -> IGlobalEvent 
#### Параметры
name [String](https://learn.microsoft.com/dotnet/api/system.string)
     Глобально уникальное имя объекта синхронизации. Не должно быть равно null или пустой строке. Обычно не зависит от регистра символов. 
#### Возвращаемое значение
[IGlobalEvent](T_Chronos_Platform_IPC_IGlobalEvent.htm)  
Событие, созданное по глобально уникальному имени. Не должно быть равно null.
#### Реализации
[IChronosPlatformDependencies.CreateGlobalEvent(String)](M_Chronos_Platform_IChronosPlatformDependencies_CreateGlobalEvent.htm)  
##  __См. также
#### Ссылки
[LinuxChronosPlatformDependencies -
](T_Chronos_Platform_LinuxChronosPlatformDependencies.htm)
[Chronos.Platform - пространство имён](N_Chronos_Platform.htm)
