# NotificationHelper.AddNotification<T>(IDictionary<String, Object>, T[]) -
метод
##  __Definition
 **Пространство имён:**
[Tessa.Extensions.Default.Shared.Notices](N_Tessa_Extensions_Default_Shared_Notices.htm)  
 **Сборка:** Tessa.Extensions.Default.Shared (в
Tessa.Extensions.Default.Shared.dll) Версия: 3.6.0.17
C# __Копировать
     public static void AddNotification<T>(
    	IDictionary<string, Object> info,
    	params T[] notifications
    )
    where T : INotification
VB __Копировать
     Public Shared Sub AddNotification(Of T As INotification) ( 
    	info As IDictionary(Of String, Object),
    	ParamArray notifications As T()
    )
C++ __Копировать
     public:
    generic<typename T>
    where T : INotification
    static void AddNotification(
    	IDictionary<String^, Object^>^ info, 
    	... array<T>^ notifications
    )
F# __Копировать
     static member AddNotification : 
            info : IDictionary<string, Object> * 
            notifications : 'T[] -> unit  when 'T : INotification
#### Параметры
info
[IDictionary](https://learn.microsoft.com/dotnet/api/system.collections.generic.idictionary-2)<[String](https://learn.microsoft.com/dotnet/api/system.string),
[Object](https://learn.microsoft.com/dotnet/api/system.object)>
notifications T[]
#### Параметры типа
T
##  __См. также
#### Ссылки
[NotificationHelper -
](T_Tessa_Extensions_Default_Shared_Notices_NotificationHelper.htm)
[AddNotification -
перегрузка](Overload_Tessa_Extensions_Default_Shared_Notices_NotificationHelper_AddNotification.htm)
[Tessa.Extensions.Default.Shared.Notices - пространство
имён](N_Tessa_Extensions_Default_Shared_Notices.htm)
