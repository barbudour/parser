# DocLoadExtensionContext - конструктор
Создаёт экземпляр класса с указанием значений его свойств.
## __Definition
 **Пространство имён:**
[Tessa.Extensions.Platform.Server.DocLoad](N_Tessa_Extensions_Platform_Server_DocLoad.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public DocLoadExtensionContext(
    	IDbScope dbScope,
    	IDocLoadSettings settings,
    	IDocLoadDocument document,
    	string inputFilePath,
    	string barcode,
    	CancellationToken cancellationToken = default
    )
VB __Копировать
     Public Sub New ( 
    	dbScope As IDbScope,
    	settings As IDocLoadSettings,
    	document As IDocLoadDocument,
    	inputFilePath As String,
    	barcode As String,
    	Optional cancellationToken As CancellationToken = Nothing
    )
C++ __Копировать
     public:
    DocLoadExtensionContext(
    	IDbScope^ dbScope, 
    	IDocLoadSettings^ settings, 
    	IDocLoadDocument^ document, 
    	String^ inputFilePath, 
    	String^ barcode, 
    	CancellationToken cancellationToken = CancellationToken()
    )
F# __Копировать
     new : 
            dbScope : IDbScope * 
            settings : IDocLoadSettings * 
            document : IDocLoadDocument * 
            inputFilePath : string * 
            barcode : string * 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> DocLoadExtensionContext
#### Параметры
dbScope [IDbScope](T_Tessa_Platform_Data_IDbScope.htm)
    Объект для взаимодействия с базой данных.
settings
[IDocLoadSettings](T_Tessa_Extensions_Platform_Server_DocLoad_IDocLoadSettings.htm)
    Настройки модуля потокового сканирования
document
[IDocLoadDocument](T_Tessa_Extensions_Platform_Server_DocLoad_IDocLoadDocument.htm)
    Документ, прикрепляемый к карточке.
inputFilePath [String](https://learn.microsoft.com/dotnet/api/system.string)
    Путь к оригинальному документу
barcode [String](https://learn.microsoft.com/dotnet/api/system.string)
    Штрих-код, распознанный на изображении.
cancellationToken
[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)
(Optional)
    Объект, посредством которого можно отменить асинхронную задачу.
##  __См. также
#### Ссылки
[DocLoadExtensionContext -
](T_Tessa_Extensions_Platform_Server_DocLoad_DocLoadExtensionContext.htm)
[Tessa.Extensions.Platform.Server.DocLoad - пространство
имён](N_Tessa_Extensions_Platform_Server_DocLoad.htm)
