# ScanDocumentType - конструктор
Создаёт экземпляр класса с указанием значений его свойств.
## __Definition
 **Пространство имён:**
[Tessa.Extensions.Platform.Client.Scanning](N_Tessa_Extensions_Platform_Client_Scanning.htm)  
 **Сборка:** Tessa.UI (в Tessa.UI.dll) Версия: 3.6.0.17
C# __Копировать
     public ScanDocumentType(
    	string name,
    	Func<IUnityContainer, ScanDocumentGenerator> getGeneratorFunc,
    	ScanDocumentTag tag = ScanDocumentTag.None,
    	string caption = null
    )
VB __Копировать
     Public Sub New ( 
    	name As String,
    	getGeneratorFunc As Func(Of IUnityContainer, ScanDocumentGenerator),
    	Optional tag As ScanDocumentTag = ScanDocumentTag.None,
    	Optional caption As String = Nothing
    )
C++ __Копировать
     public:
    ScanDocumentType(
    	String^ name, 
    	Func<IUnityContainer^, ScanDocumentGenerator^>^ getGeneratorFunc, 
    	ScanDocumentTag tag = ScanDocumentTag::None, 
    	String^ caption = nullptr
    )
F# __Копировать
     new : 
            name : string * 
            getGeneratorFunc : Func<IUnityContainer, ScanDocumentGenerator> * 
            ?tag : ScanDocumentTag * 
            ?caption : string 
    (* Defaults:
            let _tag = defaultArg tag ScanDocumentTag.None
            let _caption = defaultArg caption null
    *)
    -> ScanDocumentType
#### Параметры
name [String](https://learn.microsoft.com/dotnet/api/system.string)
     Имя формата файла, например, "PDF" или "TIFF". Отображается пользователю, если заголовок caption равен null или пустой строке. 
getGeneratorFunc
[Func](https://learn.microsoft.com/dotnet/api/system.func-2)<IUnityContainer,
[ScanDocumentGenerator](T_Tessa_Extensions_Platform_Client_Scanning_ScanDocumentGenerator.htm)>
     Функция, создающая или возвращающая объект [ScanDocumentGenerator](T_Tessa_Extensions_Platform_Client_Scanning_ScanDocumentGenerator.htm) для генерации документов. Параметром функция получает контейнер Unity, из которого могут быть получены любые требуемые зависимости. 
tag
[ScanDocumentTag](T_Tessa_Extensions_Platform_Client_Scanning_ScanDocumentTag.htm)
(Optional)
     Информация, описывающая тип генерируемого документа и выводимая рядом с именем документа. Актуальна, если заголовок caption равен null или пустой строке. 
caption [String](https://learn.microsoft.com/dotnet/api/system.string)
(Optional)
     Заголовок типа документа. Если не равен null или пустой строке, то он используется вместо описания имени типа name и тега tag. 
## __См. также
#### Ссылки
[ScanDocumentType -
](T_Tessa_Extensions_Platform_Client_Scanning_ScanDocumentType.htm)
[Tessa.Extensions.Platform.Client.Scanning - пространство
имён](N_Tessa_Extensions_Platform_Client_Scanning.htm)
