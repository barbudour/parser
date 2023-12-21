# AdEntryComparer.Equals(AdEntry, AdEntry) - метод
Сравнивает записи о составе роли по идентификаторам пользователей.
## __Definition
 **Пространство имён:**
[Tessa.Extensions.Platform.Server.AdSync](N_Tessa_Extensions_Platform_Server_AdSync.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public bool Equals(
    	AdEntry x,
    	AdEntry y
    )
VB __Копировать
     Public Function Equals ( 
    	x As AdEntry,
    	y As AdEntry
    ) As Boolean
C++ __Копировать
     public:
    virtual bool Equals(
    	AdEntry^ x, 
    	AdEntry^ y
    ) sealed
F# __Копировать
     abstract Equals : 
            x : AdEntry * 
            y : AdEntry -> bool 
    override Equals : 
            x : AdEntry * 
            y : AdEntry -> bool 
#### Параметры
x [AdEntry](T_Tessa_Extensions_Platform_Server_AdSync_AdEntry.htm)
    Первая запись.
y [AdEntry](T_Tessa_Extensions_Platform_Server_AdSync_AdEntry.htm)
    Вторая запись.
#### Возвращаемое значение
[Boolean](https://learn.microsoft.com/dotnet/api/system.boolean)  
true, если записи идентичны; false в противном случае.
#### Реализации
[IEqualityComparer<T>.Equals(T,
T)](https://learn.microsoft.com/dotnet/api/system.collections.generic.iequalitycomparer-1.equals#system-
collections-generic-iequalitycomparer-1-equals\(-0-0\))  
##  __См. также
#### Ссылки
[AdEntryComparer -
](T_Tessa_Extensions_Platform_Server_AdSync_AdEntryComparer.htm)
[Equals -
перегрузка](Overload_Tessa_Extensions_Platform_Server_AdSync_AdEntryComparer_Equals.htm)
[Tessa.Extensions.Platform.Server.AdSync - пространство
имён](N_Tessa_Extensions_Platform_Server_AdSync.htm)
