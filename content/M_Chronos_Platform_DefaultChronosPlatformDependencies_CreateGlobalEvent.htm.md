# DefaultChronosPlatformDependencies.CreateGlobalEvent - метод
Создаёт событие по глобально уникальному имени, который можно использовать для
синхронизации процессов как минимум в пределах сессии пользователя и всех
процессов в ней.
## __Definition
 **Пространство имён:** [Chronos.Platform](N_Chronos_Platform.htm)  
 **Сборка:** Chronos.Platform (в Chronos.Platform.dll) Версия: 3.6.0.17
C# __Копировать
     public virtual IGlobalEvent CreateGlobalEvent(
    	string name
    )
VB __Копировать
     Public Overridable Function CreateGlobalEvent ( 
    	name As String
    ) As IGlobalEvent
C++ __Копировать
     public:
    virtual IGlobalEvent^ CreateGlobalEvent(
    	String^ name
    )
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
[DefaultChronosPlatformDependencies -
](T_Chronos_Platform_DefaultChronosPlatformDependencies.htm)
[Chronos.Platform - пространство имён](N_Chronos_Platform.htm)
