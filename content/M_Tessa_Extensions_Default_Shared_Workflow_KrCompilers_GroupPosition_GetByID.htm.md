# GroupPosition.GetByID(Nullable<Int32>) - метод
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
    	int? id
    )
VB __Копировать
     Public Shared Function GetByID ( 
    	id As Integer?
    ) As GroupPosition
C++ __Копировать
     public:
    static GroupPosition GetByID(
    	Nullable<int> id
    )
F# __Копировать
     static member GetByID : 
            id : Nullable<int> -> GroupPosition 
#### Параметры
id
[Nullable](https://learn.microsoft.com/dotnet/api/system.nullable-1)<[Int32](https://learn.microsoft.com/dotnet/api/system.int32)>
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
