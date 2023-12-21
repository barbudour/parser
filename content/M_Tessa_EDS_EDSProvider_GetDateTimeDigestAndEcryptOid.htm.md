# EDSProvider.GetDateTimeDigestAndEcryptOid - метод
##  __Definition
 **Пространство имён:** [Tessa.EDS](N_Tessa_EDS.htm)  
 **Сборка:** Tessa.Server (в Tessa.Server.dll) Версия: 3.6.0.17
C# __Копировать
     public static (DateTime? dateTime, string encryptOid, string digestOid) GetDateTimeDigestAndEcryptOid(
    	byte[] eds
    )
VB __Копировать
     Public Shared Function GetDateTimeDigestAndEcryptOid ( 
    	eds As Byte()
    ) As (dateTime As DateTime?, encryptOid As String, digestOid As String)
C++ __Копировать
     public:
    static ValueTuple<Nullable<DateTime>, String^, String^> GetDateTimeDigestAndEcryptOid(
    	array<unsigned char>^ eds
    )
F# __Копировать
     static member GetDateTimeDigestAndEcryptOid : 
            eds : byte[] -> ValueTuple<Nullable<DateTime>, string, string> 
#### Параметры
eds [Byte](https://learn.microsoft.com/dotnet/api/system.byte)[]
#### Возвращаемое значение
[ValueTuple](https://learn.microsoft.com/dotnet/api/system.valuetuple-3)<[Nullable](https://learn.microsoft.com/dotnet/api/system.nullable-1)<[DateTime](https://learn.microsoft.com/dotnet/api/system.datetime)>,
[String](https://learn.microsoft.com/dotnet/api/system.string),
[String](https://learn.microsoft.com/dotnet/api/system.string)>
##  __См. также
#### Ссылки
[EDSProvider - ](T_Tessa_EDS_EDSProvider.htm)
[Tessa.EDS - пространство имён](N_Tessa_EDS.htm)
