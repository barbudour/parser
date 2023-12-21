# CardContentContext(Guid, Guid, Guid, CardFileSourceType,
IValidationResultBuilder) - конструктор
Создаёт экземпляр класса с указанием информации о версии файла, которая
описывает контент, и объекта, выполняющего построение результата валидации.
## __Definition
 **Пространство имён:**
[Tessa.Cards.ComponentModel](N_Tessa_Cards_ComponentModel.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public CardContentContext(
    	Guid cardID,
    	Guid fileID,
    	Guid versionRowID,
    	CardFileSourceType source,
    	IValidationResultBuilder validationResult = null
    )
VB __Копировать
     Public Sub New ( 
    	cardID As Guid,
    	fileID As Guid,
    	versionRowID As Guid,
    	source As CardFileSourceType,
    	Optional validationResult As IValidationResultBuilder = Nothing
    )
C++ __Копировать
     public:
    CardContentContext(
    	Guid cardID, 
    	Guid fileID, 
    	Guid versionRowID, 
    	CardFileSourceType source, 
    	IValidationResultBuilder^ validationResult = nullptr
    )
F# __Копировать
     new : 
            cardID : Guid * 
            fileID : Guid * 
            versionRowID : Guid * 
            source : CardFileSourceType * 
            ?validationResult : IValidationResultBuilder 
    (* Defaults:
            let _validationResult = defaultArg validationResult null
    *)
    -> CardContentContext
#### Параметры
cardID [Guid](https://learn.microsoft.com/dotnet/api/system.guid)
    Идентификатор карточки, которая содержит файл с контентом.
fileID [Guid](https://learn.microsoft.com/dotnet/api/system.guid)
    Идентификатор файла, который содержит версию с контентом.
versionRowID [Guid](https://learn.microsoft.com/dotnet/api/system.guid)
    Идентификатор версии файла, которая описывает контент.
source [CardFileSourceType](T_Tessa_Cards_CardFileSourceType.htm)
    Местоположение контента файла.
validationResult
[IValidationResultBuilder](T_Tessa_Platform_Validation_IValidationResultBuilder.htm)
(Optional)
     Объект, выполняющий построение результата валидации, или null, если создаётся новый экземпляр объекта. 
## __См. также
#### Ссылки
[CardContentContext - ](T_Tessa_Cards_ComponentModel_CardContentContext.htm)
[CardContentContext -
перегрузка](Overload_Tessa_Cards_ComponentModel_CardContentContext__ctor.htm)
[Tessa.Cards.ComponentModel - пространство
имён](N_Tessa_Cards_ComponentModel.htm)
