# GroupPosition.GetByID(Object) - метод
Возвращает объект
[GroupPosition](T_Tessa_Extensions_Default_Shared_Workflow_KrCompilers_GroupPosition.htm)
в соответствии с заданным идентификатором положения относительно этапов,
добавленных вручную.
## __Definition
 **Пространство имён:**
[Tessa.Extensions.Default.Shared.Workflow.KrCompilers](N_Tessa_Extensions_Default_Shared_Workflow_KrCompilers.htm)  
 **Сборка:** Tessa.Extensions.Default.Shared (в
Tessa.Extensions.Default.Shared.dll) Версия: 3.6.0.17
C# __Копировать
     public static GroupPosition GetByID(
    	Object id
    )
VB __Копировать
     Public Shared Function GetByID ( 
    	id As Object
    ) As GroupPosition
C++ __Копировать
     public:
    static GroupPosition GetByID(
    	Object^ id
    )
F# __Копировать
     static member GetByID : 
            id : Object -> GroupPosition 
#### Параметры
id [Object](https://learn.microsoft.com/dotnet/api/system.object)
    Идентификатор положения относительно этапов, добавленных вручную.
#### Возвращаемое значение
[GroupPosition](T_Tessa_Extensions_Default_Shared_Workflow_KrCompilers_GroupPosition.htm)  
Объект
[GroupPosition](T_Tessa_Extensions_Default_Shared_Workflow_KrCompilers_GroupPosition.htm),
соответствующий заданному идентификатору положения относительно этапов,
добавленных вручную, или значение
[Unspecified](P_Tessa_Extensions_Default_Shared_Workflow_KrCompilers_GroupPosition_Unspecified.htm),
если заданное значение не соответствует ни одному из известных положений
этапов.
##  __См. также
#### Ссылки
[GroupPosition -
](T_Tessa_Extensions_Default_Shared_Workflow_KrCompilers_GroupPosition.htm)
[GetByID -
перегрузка](Overload_Tessa_Extensions_Default_Shared_Workflow_KrCompilers_GroupPosition_GetByID.htm)
[Tessa.Extensions.Default.Shared.Workflow.KrCompilers - пространство
имён](N_Tessa_Extensions_Default_Shared_Workflow_KrCompilers.htm)
