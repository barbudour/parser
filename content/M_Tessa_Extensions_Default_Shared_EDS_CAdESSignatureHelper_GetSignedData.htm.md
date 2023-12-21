# CAdESSignatureHelper.GetSignedData - метод
##  __Definition
 **Пространство имён:**
[Tessa.Extensions.Default.Shared.EDS](N_Tessa_Extensions_Default_Shared_EDS.htm)  
 **Сборка:** Tessa.Extensions.Default.Shared (в
Tessa.Extensions.Default.Shared.dll) Версия: 3.6.0.17
C# __Копировать
     public static SignedData GetSignedData(
    	CardResponse response,
    	bool withoutValidationInfos = false
    )
VB __Копировать
     Public Shared Function GetSignedData ( 
    	response As CardResponse,
    	Optional withoutValidationInfos As Boolean = false
    ) As SignedData
C++ __Копировать
     public:
    static SignedData^ GetSignedData(
    	CardResponse^ response, 
    	bool withoutValidationInfos = false
    )
F# __Копировать
     static member GetSignedData : 
            response : CardResponse * 
            ?withoutValidationInfos : bool 
    (* Defaults:
            let _withoutValidationInfos = defaultArg withoutValidationInfos false
    *)
    -> SignedData 
#### Параметры
response [CardResponse](T_Tessa_Cards_CardResponse.htm)
withoutValidationInfos
[Boolean](https://learn.microsoft.com/dotnet/api/system.boolean) (Optional)
#### Возвращаемое значение
[SignedData](T_Tessa_Platform_EDS_SignedData.htm)
##  __См. также
#### Ссылки
[CAdESSignatureHelper -
](T_Tessa_Extensions_Default_Shared_EDS_CAdESSignatureHelper.htm)
[Tessa.Extensions.Default.Shared.EDS - пространство
имён](N_Tessa_Extensions_Default_Shared_EDS.htm)
