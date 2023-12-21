# NotificationHelper.AddNotification<T>(CardInfoStorageObject, T[]) - метод
##  __Definition
 **Пространство имён:**
[Tessa.Extensions.Default.Shared.Notices](N_Tessa_Extensions_Default_Shared_Notices.htm)  
 **Сборка:** Tessa.Extensions.Default.Shared (в
Tessa.Extensions.Default.Shared.dll) Версия: 3.6.0.17
C# __Копировать
     public static void AddNotification<T>(
    	CardInfoStorageObject infoObject,
    	params T[] notifications
    )
    where T : INotification
VB __Копировать
     Public Shared Sub AddNotification(Of T As INotification) ( 
    	infoObject As CardInfoStorageObject,
    	ParamArray notifications As T()
    )
C++ __Копировать
     public:
    generic<typename T>
    where T : INotification
    static void AddNotification(
    	CardInfoStorageObject^ infoObject, 
    	... array<T>^ notifications
    )
F# __Копировать
     static member AddNotification : 
            infoObject : CardInfoStorageObject * 
            notifications : 'T[] -> unit  when 'T : INotification
#### Параметры
infoObject [CardInfoStorageObject](T_Tessa_Cards_CardInfoStorageObject.htm)
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
