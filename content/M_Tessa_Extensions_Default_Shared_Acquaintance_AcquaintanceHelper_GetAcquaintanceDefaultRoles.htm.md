# AcquaintanceHelper.GetAcquaintanceDefaultRoles - метод
Получение ролей по умолчанию для массового ознакомления
## __Definition
 **Пространство имён:**
[Tessa.Extensions.Default.Shared.Acquaintance](N_Tessa_Extensions_Default_Shared_Acquaintance.htm)  
 **Сборка:** Tessa.Extensions.Default.Shared (в
Tessa.Extensions.Default.Shared.dll) Версия: 3.6.0.17
C# __Копировать
     public static List<Tuple<Guid, string>> GetAcquaintanceDefaultRoles(
    	Dictionary<string, Object> info
    )
VB __Копировать
     Public Shared Function GetAcquaintanceDefaultRoles ( 
    	info As Dictionary(Of String, Object)
    ) As List(Of Tuple(Of Guid, String))
C++ __Копировать
     public:
    static List<Tuple<Guid, String^>^>^ GetAcquaintanceDefaultRoles(
    	Dictionary<String^, Object^>^ info
    )
F# __Копировать
     static member GetAcquaintanceDefaultRoles : 
            info : Dictionary<string, Object> -> List<Tuple<Guid, string>> 
#### Параметры
info
[Dictionary](https://learn.microsoft.com/dotnet/api/system.collections.generic.dictionary-2)<[String](https://learn.microsoft.com/dotnet/api/system.string),
[Object](https://learn.microsoft.com/dotnet/api/system.object)>
    Info с данными
#### Возвращаемое значение
[List](https://learn.microsoft.com/dotnet/api/system.collections.generic.list-1)<[Tuple](https://learn.microsoft.com/dotnet/api/system.tuple-2)<[Guid](https://learn.microsoft.com/dotnet/api/system.guid),
[String](https://learn.microsoft.com/dotnet/api/system.string)>>  
Список ролей с идентификаторами
##  __См. также
#### Ссылки
[AcquaintanceHelper -
](T_Tessa_Extensions_Default_Shared_Acquaintance_AcquaintanceHelper.htm)
[Tessa.Extensions.Default.Shared.Acquaintance - пространство
имён](N_Tessa_Extensions_Default_Shared_Acquaintance.htm)
